function FormValidation(FormObj) {
    // Form data stored as variables
    let FName = FormObj.elements.item(1).value;
    let LName = FormObj.elements.item(2).value; 
    let Email = FormObj.elements.item(3).value;
    let DateOfSub = new Date(FormObj.elements.item(4).value);
    let Description = FormObj.elements.item(5).value;

    // Other variables
    let Errors = "";
    let NoErrors = true;
    let CurrentDate = new Date();
    let ErrorMessages = [
        " - First name must be given!",
        " - Last name must be given!",
        " - Date must be given!",
        " - Email must be given",
        " - The email must have a single \"@\"!",
        " - The email must have at least 1 \".\"!",
        " - A description must be given!"        
    ]

    // Error Checking and logs it
    // alert(typeof DateOfSub.getFullYear); // Used to debug the types of variables so can properly be compared
    // alert(typeof DateOfSub.getFullYear());
    // Names √
    if ((FName == "") && (FName.length >= 3)) {
        Errors += (Errors == "") ? ErrorMessages[0] : "\n${ErrorMessages[0]}";
        NoErrors = false;
    };
    if ((LName == "") && (FName.length >= 3)) {
        Errors += (Errors == "") ? ErrorMessages[1] : "\n${ErrorMessages[1]}";
        NoErrors = false;
    };
    // Date
    if (DateOfSub == "") {
        Errors += (Errors == "") ? ErrorMessages[2] : "\n${ErrorMessages[2]}";
        NoErrors = false;
    }
    // Email √
    if (Email == "") {
        Errors += (Errors == "") ? ErrorMessages[3] : "\n${ErrorMessages[3]}";
        NoErrors = false;
    }
    else {
        if ((!Email.includes("@", 1)) && (Email.length >= 5)) { // Starts after the first character since there has to be something on both sides of the @
            Errors += (Errors == "") ? ErrorMessages[4] : "\n${ErrorMessages[4]}";
            NoErrors = false;
        }
        if (!Email.includes(".", 1)) {
            Errors += (Errors == "") ? ErrorMessages[5] : "\n${ErrorMessages[5]}";
            NoErrors = false;
        }
    }
    // Textarea √
    if (Description == "") {
        Errors += (Errors == "") ? ErrorMessages[6] : "\n${ErrorMessages[6]}";
        NoErrors = false;
    }

    // Sends data off if valid
    if (NoErrors) {
        if ((FName == "Ralfs") && (LName == "Varpins")) {
            document.getElementById("OutBox").innerHTML = "Hello Mr 10K questions 🏆";
        }
        else {
            [NoErrors, FName, LName, Email, DateOfSub, Description];
            document.getElementById("OutBox").innerHTML = `Thank you ${FName.slice(0, 3)}${LName.slice(0, 3)} for submitting the form at ${DateOfSub.toLocaleDateString("en-UK")}`;
        }
    }
    else {
        alert(Errors);
    }
}

document.addEventListener("DOMContentLoaded", function(event) { // On loading of full page, runs code
    const Form = document.getElementById("FormName");           // Identifies form

    Form.addEventListener("submit", function(event) {           // Executes code when the Form is submitted
        alert("please work");                                   // Encourages the code to work
        event.preventDefault();                                 // When submitted, prevents page from refreshing/updating?
        FormValidation(Form);                                   // Validation
        alert("This code has ran");
    });
});

/*
 # Requirements : 
 
 + Input validation
 - All inputs must be given
 - Email must have at least 1 "." and at least 1 "@"
 - Date must be in DD/MM/YYYY form and a suitable date (01/01/1900)

 + Output
 - Alert `Thank you for completing the form.\n${FirstName[0:3] + SecondName[0:3]}`
 - Probably store or send off data somehow

 + Easter egg
 - If name is Ralfs Varpins, alert : sod off Mr 10K SRQ
 - Reset textarea if length >1,000 char
*/


/*
let TextArea = document.getElementById("TextBox");
TextArea.addEventListener("input", function() {
    if (this.value.length >= 10) {
        this.value = "Too full! BURPP";
    }
});
*/