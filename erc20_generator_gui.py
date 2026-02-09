import tkinter as tk
from tkinter import messagebox

class ERC20GeneratorGUI:
    def __init__(self, root):
        # WINDOW
        self.root = root
        self.root.title("ERC20 Token Generator – GUI Demo")
        self.root.geometry("650x600")

        # TITLE
        tk.Label(root, text="ERC20 Token Generator (GUI)",
                 font=("Arial",16,"bold")).pack(pady=10)

        # INPUTS
        tk.Label(root, text="Token Name").pack()
        self.name_entry = tk.Entry(root, width=60)
        self.name_entry.pack(pady=5)

        tk.Label(root, text="Token Symbol").pack()
        self.symbol_entry = tk.Entry(root, width=60)
        self.symbol_entry.pack(pady=5)

        tk.Label(root, text="Initial Supply").pack()
        self.supply_entry = tk.Entry(root, width=60)
        self.supply_entry.pack(pady=5)

        tk.Label(root, text="Decimals (18 recommended)").pack()
        self.decimals_entry = tk.Entry(root, width=60)
        self.decimals_entry.pack(pady=5)

        # BUTTONS
        tk.Button(root, text="Generate ERC20 Contract",
                  command=self.generate_contract,
                  bg="lightblue", width=25).pack(pady=6)

        tk.Button(root, text="Clear History",
                  command=self.clear_output,
                  bg="lightcoral", width=25).pack(pady=6)

        # OUTPUT BOX
        self.output = tk.Text(root, height=18, width=78)
        self.output.pack(pady=10)

        self.show_start_log()

    # START LOG
    def show_start_log(self):
        self.output.insert(tk.END, "APPLICATION STARTED\n")
        self.output.insert(tk.END, "-"*65 + "\n")
        self.output.insert(tk.END, "This app generates ERC20 Smart Contracts\n\n")

    # GENERATE CONTRACT FUNCTION
    def generate_contract(self):
        name = self.name_entry.get()
        symbol = self.symbol_entry.get()
        supply = self.supply_entry.get()
        decimals = self.decimals_entry.get()

        if name=="" or symbol=="" or supply=="" or decimals=="":
            messagebox.showwarning("Warning","Fill all fields")
            return

        solidity_code = f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract {name} {{
    string public name = "{name}";
    string public symbol = "{symbol}";
    uint8 public decimals = {decimals};
    uint public totalSupply;

    mapping(address => uint) public balanceOf;

    event Transfer(address indexed from, address indexed to, uint value);

    constructor() {{
        totalSupply = {supply} * 10 ** uint(decimals);
        balanceOf[msg.sender] = totalSupply;
    }}

    function transfer(address to, uint value) public returns (bool) {{
        require(balanceOf[msg.sender] >= value, "Insufficient balance");
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }}
}}
"""

        filename = name + ".sol"
        with open(filename, "w") as f:
            f.write(solidity_code)

        self.output.insert(tk.END, "-"*65 + "\n")
        self.output.insert(tk.END, "Function Called: generate_contract()\n")
        self.output.insert(tk.END, f"File Created: {filename}\n\n")

        messagebox.showinfo("Success", filename + " created successfully!")

    # CLEAR OUTPUT
    def clear_output(self):
        self.output.delete(1.0, tk.END)
        self.show_start_log()

# MAIN
if __name__ == "__main__":
    root = tk.Tk()
    app = ERC20GeneratorGUI(root)
    root.mainloop()
