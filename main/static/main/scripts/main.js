// Сумарні значення змінних
let pushUpsTotal = document.getElementById('pushUpsNum');
let squadsTotal = document.getElementById('squadsNum');
let sitUpsTotal = document.getElementById('sitUpsNum');

// Формs
const pushUpsForm = document.getElementById('pushUpsForm');
const sitUpsForm = document.getElementById('sitUpsForm');
const squadsForm = document.getElementById('squadsForm');

// function getCookie(name) {
//   let matches = document.cookie.match(new RegExp(
//     "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
//   ));
//   return matches ? decodeURIComponent(matches[1]) : undefined;
// }

function addRecord(form, total, repsID) {
    form.addEventListener('submit', function () {
        const exerciseReps = document.getElementById(String(repsID)).value;
        let totalValue = parseInt(total.innerText); // Текст у ціле число
        if (isNaN(parseInt(exerciseReps)) === true) {
            totalValue = totalValue;
        }
        else {
            totalValue += parseInt(exerciseReps); // Додати введені дані до загальної кількості
            total.innerText = totalValue; //  Виводить суму на екран
            form.reset();
        }

        console.log('Total:', totalValue);
    })
}

addRecord(pushUpsForm, pushUpsTotal, 'repsPush');
addRecord(sitUpsForm, sitUpsTotal, 'repsSit');
addRecord(squadsForm, squadsTotal, 'repsSquad');
