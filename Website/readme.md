
### SAVING FORM DATA INTO A CSV FILE

It doesn't make a lot of sense bcs we are going to upload the csv among the web files and won't have access to csv when project is deployed

We can use PythonAnywhere that allows to host a site having access to all files while it's deployed so you'd be able to see data returned from form in csv file

```py
def write_to_csv(data):
    with open('database.csv',mode="a",newline="") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email,subject,message])
```

___

### SAVING FORM DATA INTO GOOGLE DRIVE

I prefer to send Form data into an existing excel file from Google Drive, this way just need to open Excel file to see if there's new data.

- Form tag id -> #sheedtb-form

- Form method = 'POST'

- Form action="WRITE_HERE_YOUR_GOOGLE_DRIVE_EXCEL_URL" 


```HTML
<form id="sheedtb-form" method="POST" action="WRITE_HERE_YOUR_GOOGLE_DRIVE_EXCEL_URL">

    ...
    
</form>
```

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
      // you can put any JS code here, this case is returning Thankyou Page
      location.href='./thankyou.html'
    });
  });

```

Don't forget imports (I do always forget)

```py
from flask import Flask, render_template, url_for, request, redirect
import csv
```
