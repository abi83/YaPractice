/*
The function should check if name is an actual contact's firstName and
the given property (prop) is a property of that contact.

If both are true, then return the "value" of that property.

If name does not correspond to any contacts then return "No such contact".

If prop does not correspond to any valid properties of a contact found to
match name then return "No such property".
*/

// Setup
var contacts = [
    {
        "firstName": "Akira",
        "lastName": "Laine",
        "number": "0543236543",
        "likes": ["Pizza", "Coding", "Brownie Points"]
    },
    {
        "firstName": "Harry",
        "lastName": "Potter",
        "number": "0994372684",
        "likes": ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "0487345643",
        "likes": ["Intriguing Cases", "Violin"]
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["JavaScript", "Gaming", "Foxes"]
    }
];


function lookUpProfile(name, prop){
// Only change code below this line
    var nameFound = false;
    var propFound = false;
    for (var element of contacts) {
//        console.log(element);
//        console.log(element.firstName == name);
//        console.log(element.hasOwnProperty(prop));

        if (element.firstName == name) {nameFound = true;}
        if (element.hasOwnProperty(prop)) {propFound = true;}

        if (element.firstName == name && element.hasOwnProperty(prop)) {
//            console.log(element[prop]);
            return element[prop];
        }
    }
    if (!nameFound) {return 'No such contact'}
    if (!propFound) {return 'No such property'}

// Only change code above this line
}
console.log(lookUpProfile("Kristian", "lastName"))
console.log(lookUpProfile("Sherlock", "likes"))
console.log(lookUpProfile("Harry", "likes"))
console.log(lookUpProfile("Bob", "number"))
console.log(lookUpProfile("Bob", "potato"))
console.log(lookUpProfile("Akira", "address"))




//lookUpProfile("Akira", "likes");