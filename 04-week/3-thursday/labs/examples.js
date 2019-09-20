var res = [3, 4, -6, 0, -8, -1, 3, -6, 1, -8, -6, -1, 8, 10, 18];
//get positive negative values
var pos = res.filter(function(v) {
    
console.log(res);
});

var even_numbers = res.filter(item => item % 2 == 2);
console.log(even_numbers);


var square_numbers = res.filter(item => item * item);
console.log(square_numbers);

console.groupEnd();

var cities = [
    { name: 'Los Angeles', temperature: 60.0},
    { name: 'Atlanta', temperature: 52.0 },
    { name: 'Detroit', temperature: 48.0 },
    { name: 'New York', temperature: 80.0 } ];

var cool_cities = cities.filter(temperature => temperature > 70.0);
console.log(cool_cities);

var name_cities = cities.filter(name => name);
console.log(name_cities);


console.groupEnd();

var people = [ 'Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur', 'Jason', 'Che', 'Ben' ];
var peoples_names = people.forEach(name =>name);
console.log('Good Job! {{name}}');

var peoplesNames = people.sort(name => name);
console.log(people);

var peoplesName = people.sort(name => name);
console.log(people);

people.sort();
console.log(people);

console.groupEnd();


var arr = [[1, 3, 4],[2, 4, 6, 8],[3, 6] ];
    
var addIndexes = arr.addIndexes[0][1][2]
console.log(addIndexes)