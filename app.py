from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Roll number with names
students = {
    1: "Akash Shalom",
    2: "Abinaya R",
    3: "Abinaya S (8.2)",
    4: "Abinaya S (1.4)",
    5: "Ajeez",
    6: "Ajin Durai",
    7: "Akash",
    8: "Akshaya",
    9: "Alagu Lakshmanan",
    10: "Ancy Infant Jemi",
    12: "Anusha",
    13: "Arockiya Varsha",
    14: "Arockiya Abisha",
    15: "Ashok Kumar",
    16: "Banu Priya",
    17: "Bavithra",
    18: "Bindhuja",
    19: "Brajesh",
    21: "Tharwin",
    22: "Edwin Durai",
    23: "Essakiammal",
    24: "Esakki Durai",
    25: "Gopalakrishnan",
    26: "Hemalatha",
    27: "Hephzibha",
    28: "Hirthik",
    29: "Indhumathi",
    30: "Ishwarya",
    31: "Kajitha",
    32: "Kanisha",
    33: "Karthikeyan",
    34: "Kaushalya",
    35: "Keerthika",
    36: "Kirubakaran",
    37: "Lakshmi",
    38: "Lakshmi Manohari",
    39: "Latika Shalin",
    40: "Linga Arasi",
    41: "Madhumitha",
    42: "Mahalakshmi",
    44: "Manikandan",
    45: "Manju"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate_number():
    excluded = [11, 20, 43]
    number = random.randint(1, 45)

    while number in excluded:
        number = random.randint(1, 45)

    name = students.get(number, "Name not found")

    return jsonify({
        "roll_number": number,
        "name": name
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)