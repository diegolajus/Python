# SAVING FORM DATA INTO A CSV FILE
# IT DOESN'T MAKE A LOT OF SENSE BCS WE ARE GOING TO UPLOAD THE CSV AS A WEB FILE AND WE HAVE NO ACCESS TO IT WHEN IT IS DEPLOYED
# WE CAN USE PYTHONANYWHERE THAT ALLOOWS TO HOST A SITE HAVING ACCES TO ALL FILES WHILE IT'S DEPLOYED SO YOU'D BE ABLE TO SEE DATA RETURNED FROM FORM

```py
def write_to_csv(data):
    with open('database.csv',mode="a",newline="") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email,subject,message])
```

# I PREFER TO SEND FORM DATA INTO AN EXISTING EXCEL FILE FROM GOOGLE DRIVE, THIS WAY JUST NEED TO OPEN EXCEL FILE TO SEE IF THERE'S NEW DATA

```JS

  document.addEventListener("DOMContentLoaded", function (event) {
     navActivePage();
  });

  var form = document.getElementById('sheetdb-form');
  form.addEventListener("submit", e => {
    e.preventDefault();
    fetch(form.action, {
        method : "POST",
        body: new FormData(document.getElementById("sheetdb-form")),
    }).then(
        response => response.json()
    ).then((html) => {
      // you can put any JS code here
      location.href='./thankyou.html'
    });
  });

```