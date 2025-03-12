Form = document.getElementById("Form")

Form.addEventListener("submit", () => {
    console.log(Form.getAttributes());
});

/*
function SubmitData() {
    var form = getElementsById("Form");
    console.log(`Thank you for submitting to this form ${form}`);
}

form.addEventListener("submit", (event) => { // No idea how this line works
    event.preventDefault(); // Or this...
    SubmitData();
});
*/








/*Idea : When user types close to 1000 chars (element.keyup), turn red and show a warning (alert)
When reach 1111 then delete text area content -> element.innerText = "";

The calender sets today as default*/

// alert("help");

/* function FormGetCurrentDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    const CurrentDate = `${year}-${month}-${day}`;
    document.getElementById("DateOfVisit").setAttribute("max", CurrentDate);
    alert(CurrentDate);
} 
*/