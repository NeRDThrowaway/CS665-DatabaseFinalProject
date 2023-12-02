import sqlite3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.font as tkFont

class TableWindow(tk.Toplevel):
    def __init__(self, master, table_name, cursor):
        super().__init__(master)
        self.title(f"Table: {table_name}")

        # Fetch column information using PRAGMA table_info
        column_info = cursor.execute(f"PRAGMA table_info({table_name});").fetchall()

        # Extract column names and descriptors
        column_names = [column[1] for column in column_info]
        column_descriptors = [column[2] for column in column_info]

        # Determine the maximum length of each descriptor
        max_descriptor_length = max(len(descriptor) for descriptor in column_descriptors)

        # Table listbox with horizontal and vertical scrollbars
        self.table_listbox = tk.Listbox(self, height=30, width=160, exportselection=0)
        self.table_listbox.pack(fill=tk.BOTH, expand=True)

        # Display descriptors above the data with appropriate spacing
        descriptor_row = "".join(f"{descriptor:<{max_descriptor_length + 2}}" for descriptor in column_descriptors)
        self.table_listbox.insert(tk.END, descriptor_row)

        # Fetch and display table entries
        entries = cursor.execute(f"SELECT * FROM {table_name};").fetchall()
        for entry in entries:
            # Format the data to align it properly under each descriptor
            entry_with_spacing = "".join(f"{str(value):<{max_descriptor_length + 2}}" for value in entry)
            self.table_listbox.insert(tk.END, entry_with_spacing)

        # Add horizontal scrollbar
        h_scrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.table_listbox.xview)
        self.table_listbox.configure(xscrollcommand=h_scrollbar.set)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Add vertical scrollbar
        v_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.table_listbox.yview)
        self.table_listbox.configure(yscrollcommand=v_scrollbar.set)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

class SQLiteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite GUI")

        # Create a frame
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Database file label and entry
        ttk.Label(self.frame, text="Database File:").grid(row=0, column=0, sticky=tk.W)
        self.db_entry = ttk.Entry(self.frame, width=30)
        self.db_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(self.frame, text="Open Database", command=self.open_database).grid(row=0, column=2, padx=5)

        # Table listbox
        ttk.Label(self.frame, text="Tables:").grid(row=1, column=0, sticky=tk.W)
        self.table_listbox = tk.Listbox(self.frame, height=5)
        self.table_listbox.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        self.table_listbox.bind("<ButtonRelease-1>", self.display_table)

        # Other tables listbox
        ttk.Label(self.frame, text="Other Tables:").grid(row=1, column=2, sticky=tk.W)
        self.other_tables_listbox = tk.Listbox(self.frame, height=5)
        self.other_tables_listbox.grid(row=1, column=3, sticky=(tk.W, tk.E), pady=5)

        # SQL statement entry
        ttk.Label(self.frame, text="SQL Statement:").grid(row=2, column=0, sticky=tk.W)
        self.sql_entry = tk.Text(self.frame, height=5, width=50)
        self.sql_entry.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # Commit button
        ttk.Button(self.frame, text="Commit", command=self.execute_sql).grid(row=3, column=1, pady=5)

        # Save button
        ttk.Button(self.frame, text="Save", command=self.save_changes).grid(row=3, column=2, pady=5)
        
        # "Show Games Bought by Customers" button
        ttk.Button(self.frame, text="Show Games Bought by Customers", command=self.show_games_bought).grid(row=4, column=0, columnspan=3, pady=5)

        # Employee sells game button
        ttk.Button(self.frame, text="Employee Sells Game", command=self.show_games_sold).grid(row=5, column=0, columnspan=3, pady=5)
        
        # Employee sells game button
        ttk.Button(self.frame, text="When Customer Purchased", command=self.show_when_games_sold).grid(row=6, column=0, columnspan=3, pady=5)
        
        # Variables to store selected table and other tables
        self.selected_table = tk.StringVar()
        self.other_tables = tk.StringVar()

        # Database connection and cursor
        self.conn = None
        self.cursor = None

        # Flag to check if changes have been made
        self.changes_made = False

        # Set up the standard font
        self.standard_font = tkFont.nametofont("TkDefaultFont").actual()

        # Bind the switch_table method to the listbox
        self.switch_table = lambda event: self._switch_table(event)
        self.other_tables_listbox.bind("<ButtonRelease-1>", self.switch_table)

    def open_database(self):
        # Open file dialog to select SQLite database file
        db_file = filedialog.askopenfilename(filetypes=[("SQLite Database", "*.db")])
        if db_file:
            self.db_entry.delete(0, tk.END)
            self.db_entry.insert(0, db_file)

            # Open the SQLite database file
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()

            # Get and display tables
            tables = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
            self.table_listbox.delete(0, tk.END)
            self.other_tables_listbox.delete(0, tk.END)
            for table in tables:
                self.table_listbox.insert(tk.END, table[0])
                self.other_tables_listbox.insert(tk.END, table[0])

            # Display the first table with its current contents
            first_table = tables[0][0]
            self.selected_table.set(first_table)
            self.display_table_contents(first_table)

            # Reset the changes made flag
            self.changes_made = False

    def display_table(self, event):
        # Get the selected table and display its content
        selected_table = self.table_listbox.get(self.table_listbox.curselection())
        self.selected_table.set(selected_table)
        self.display_table_contents(selected_table)

    def display_table_contents(self, table_name):
        # Check if a table is selected
        if not table_name:
            return

        # Fetch column names using PRAGMA table_info
        column_info = self.cursor.execute(f"PRAGMA table_info({table_name});").fetchall()
        column_names = [column[1] for column in column_info]
        num_columns = len(column_names)

        # Clear the previous entries in the main window "table"
        self.table_listbox.delete(0, tk.END)

        # Display column names above the data with spacing
        column_names_with_spacing = "\t".join(f"{name:<15}" for name in column_names)
        self.table_listbox.insert(tk.END, column_names_with_spacing)

        # Fetch and display table entries
        entries = self.cursor.execute(f"SELECT * FROM {table_name};").fetchall()

        # Insert the new entries in the main window "table" with spacing
        for entry in entries:
            entry_with_spacing = "\t".join(f"{str(value):<15}" for value in entry)
            self.table_listbox.insert(tk.END, entry_with_spacing)

    def _switch_table(self, event):
        # Switch the displayed table when a different table is selected from "Other Tables"
        selected_table = self.other_tables_listbox.get(self.other_tables_listbox.curselection())
        self.selected_table.set(selected_table)
        self.display_table_contents(selected_table)

    def execute_sql(self):
        # Execute the SQL statement
        sql_statement = self.sql_entry.get("1.0", tk.END)
        try:
            self.cursor.execute(sql_statement)
            self.conn.commit()
            messagebox.showinfo("Success", "SQL statement executed successfully.")
            # Check if the executed SQL involves creating or deleting a table
            if "CREATE TABLE" in sql_statement or "DROP TABLE" in sql_statement:
                # Update the list of tables
                self.update_table_list()
            # Set the changes made flag to True
            self.changes_made = True
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error executing SQL statement: {e}")

    def save_changes(self):
        if not self.conn:
            messagebox.showwarning("Warning", "No database is currently open.")
            return

        if not self.changes_made:
            messagebox.showinfo("Info", "No changes to save.")
            return

        # Save changes to the database file
        try:
            self.conn.commit()
            messagebox.showinfo("Success", "Changes saved successfully.")
            # Reset the changes made flag
            self.changes_made = False
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error saving changes: {e}")

        # Update the list of tables after saving changes
        self.update_table_list()

    def update_table_list(self):
        # Update the list of tables in the "Other Tables" listbox
        tables = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        self.other_tables_listbox.delete(0, tk.END)
        for table in tables:
            self.other_tables_listbox.insert(tk.END, table[0])
    def show_games_bought(self):
        try:
            query = """
                SELECT Customers.f_name as CustomerName, Games.Name as Purchased_Game 
                FROM Games
                INNER JOIN Customers
                ON Game_bought = Game_ID;
            """
            results = self.cursor.execute(query).fetchall()

            # Clear the current table window before displaying new results
            self.table_listbox.delete(0, tk.END)

            # Display the column names
            column_names = ["CustomerName", "Purchased_Game"]
            column_names_with_spacing = "\t".join(f"{name:<15}" for name in column_names)
            self.table_listbox.insert(tk.END, column_names_with_spacing)

            # Display the results with appropriate spacing
            for entry in results:
                entry_with_spacing = "\t".join(f"{str(value):<15}" for value in entry)
                self.table_listbox.insert(tk.END, entry_with_spacing)

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error executing SQL statement: {e}")

    def show_games_sold(self):
        try:
            query = """
                SELECT Employee.emp_fname as Employee_Name, Games.Name as Game_Sold
                FROM Games
                INNER JOIN Employee
                ON Sold_by = emp_id;
            """
            results = self.cursor.execute(query).fetchall()

            # Clear the current table window before displaying new results
            self.table_listbox.delete(0, tk.END)

            # Display the column names
            column_names = ["Employee_Name", "Game_Sold"]
            column_names_with_spacing = "\t".join(f"{name:<15}" for name in column_names)
            self.table_listbox.insert(tk.END, column_names_with_spacing)

            # Display the results with appropriate spacing
            for entry in results:
                entry_with_spacing = "\t".join(f"{str(value):<15}" for value in entry)
                self.table_listbox.insert(tk.END, entry_with_spacing)

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error executing SQL statement: {e}")  

    def show_when_games_sold(self):
        try:
            query = """
                SELECT Payments.trans_datetime, Customers.f_name as Customer
                FROM Payments
                Inner JOIN Customers
                ON customerID = cust_id;
            """
            results = self.cursor.execute(query).fetchall()

            # Clear the current table window before displaying new results
            self.table_listbox.delete(0, tk.END)

            # Display the column names
            column_names = ["Date_Purchased", "Customer"]
            column_names_with_spacing = "\t".join(f"{name:<15}" for name in column_names)
            self.table_listbox.insert(tk.END, column_names_with_spacing)

            # Display the results with appropriate spacing
            for entry in results:
                entry_with_spacing = "\t".join(f"{str(value):<15}" for value in entry)
                self.table_listbox.insert(tk.END, entry_with_spacing)

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error executing SQL statement: {e}")  


if __name__ == "__main__":
    root = tk.Tk()
    app = SQLiteGUI(root)
    root.mainloop()
