import tkinter as tk
from tkinter import messagebox

class AfApp:
    def __init__(self, root):
        self.Letters = ["C", "U", "Z"]
        self.input = tk.StringVar()
        self.input.trace_add("write", self.handle_input_change)

        root.title("CURP")
        root.geometry("800x400")

        # Crear el marco principal
        main_frame = tk.Frame(root, bg="lightgray")
        main_frame.pack(expand=True, fill="both")

        # Crear el marco para la entrada
        input_frame = tk.Frame(main_frame, bg="lightgray")
        input_frame.pack(pady=(50, 10))

        label = tk.Label(input_frame, text="Validar solo cadena 'CUZC'", font=("Arial", 16), bg="lightgray")
        label.pack(pady=10)

        entry = tk.Entry(input_frame, textvariable=self.input, font=("Arial", 14), fg="black")
        entry.pack(pady=10)

        # Crear el lienzo para el gráfico
        self.canvas = tk.Canvas(main_frame, bg="white", width=800, height=200)
        self.canvas.pack()

        # Crear el botón de validación
        validate_button = tk.Button(main_frame, text="Validar", command=self.validate_input)
        validate_button.pack(pady=10)

    def handle_input_change(self, *args):
        value = self.input.get().upper()
        if len(value) <= 4 and all(char in self.Letters for char in value) and value.startswith('C'):
            self.draw_states_and_arrows(value)

    def draw_states_and_arrows(self, input_str):
        self.canvas.delete("all")
        num_states = min(5, len(input_str) + 1)
        state_radius = 30
        state_x = 100
        state_y = 100
        state_distance = 150

        for i in range(num_states):
            self.canvas.create_oval(state_x, state_y, state_x + 2*state_radius, state_y + 2*state_radius, outline="black", fill="lightgreen")
            self.canvas.create_text(state_x + state_radius, state_y + state_radius, text=f"q{i}", fill="black", font=("Arial", 14))

            if i < num_states - 1:
                self.canvas.create_line(state_x + 2*state_radius, state_y + state_radius, state_x + 2*state_radius + state_distance, state_y + state_radius, fill="green", width=2, arrow=tk.LAST)
                self.canvas.create_text(state_x + 2*state_radius + state_distance//2, state_y + state_radius - 20, text=input_str[i].upper(), fill="white", font=("Arial", 14))
                self.canvas.create_text(state_x + 2*state_radius + state_distance//2, state_y + state_radius + 20, text=input_str[i].upper(), fill="black", font=("Arial", 14))

            state_x += state_distance

    def validate_input(self):
        value = self.input.get().upper()
        if all(char in ["C", "U", "Z"] for char in value):
            messagebox.showinfo("Validación", "La cadena es válida")
        else:
            messagebox.showerror("Validación", "La cadena es inválida")

if __name__ == "__main__":
    root = tk.Tk()
    app = AfApp(root)
    root.mainloop()
