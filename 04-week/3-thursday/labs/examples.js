var num = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];

function positiveNumbers(arr){
    return arr.filter(num =>  num > 0)
}
console.log(positiveNumbers(num));

function evenNumbers(arr){

    return arr.filter(num  => num %2 == 0);
}
console.log(evenNumbers(num));

function squareNumbers(arr){

    return arr.map(num => num * num);

}
console.log(squareNumbers(num));

console.groupEnd();

var cities = [
    { name: 'Los Angeles', temperature: 60.0},
    { name: 'Atlanta', temperature: 52.0 },
    { name: 'Detroit', temperature: 48.0 },
    { name: 'New York', temperature: 80.0 } ];

function arrayCities(arr){

    return arr.filter(x => x.temperature < 70);

}
console.log(arrayCities(cities));

function nameCities(arr){

    return arr.map(x => x.name);

}
console.log(nameCities(cities));


var people = [ 'Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur', 'Jason', 'Che', 'Ben' ]; 

function peoplesName(arr){

    return arr.forEach(x => console.log(`Good Job, ${x}!`));
}

console.log(peoplesName);
