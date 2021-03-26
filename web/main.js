function addition(){
    const data1 = document.getElementById("change_total").value;
    const data2 = document.getElementById("transaction_type").value;
    const data3 = document.getElementById("reason").value;
    const data4 = document.getElementById("date").value;
    eel.add(data1, data2, data3, data4)(callBack)
}

function callBack(result){
    document.getElementById("ans").value=result
}


async function my_func() {
    let row = await eel.my_func()();
    (r = confirm("are you sure you want to delete: " + row));
    if (r === true) {
        eel.delete_row()
    }
}

async function new_function() {
    let x = await eel.new_function()();
    let z = 'current balance: ' + x;
    const str = document.getElementById("balance").innerHTML;
    document.getElementById("balance").innerHTML = str.replace('current balance:', z)
}




