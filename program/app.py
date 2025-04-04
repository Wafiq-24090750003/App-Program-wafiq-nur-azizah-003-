from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    er = None
    error_message = None

    if request.method == "POST":
        try:
            rating = int(request.form["rating"])
            ulasan = int(request.form["ulasan"])
            shares = int(request.form["shares"])
            berlangganan = int(request.form["berlangganan"])

            if berlangganan == 0:
                error_message = "Total berlangganan tidak boleh 0!"
            else:
                er = ((rating + ulasan + shares) / berlangganan) * 100
                er = round(er, 2)

        except ValueError:
            error_message = "Input tidak valid! Masukkan angka yang benar."
        except Exception as e:
            error_message = f"Terjadi kesalahan: {e}"

    return render_template("index.html", er=er, error_message=error_message)

if __name__ == "_main_":
           app.run(debug=True)