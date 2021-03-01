const p = Promise.resolve(1);
// const p = Promise.reject("failed");
// const p = fetch("http://dsfsdafasdf.com");
p
    .then(function(result) { return result + 1 })
    .then(function(result) { return result + 1 })
    .then(function(result) { return result + 1 })
    .then(function(result) { return result + 1 })
    .then(function(result) { return result + 1 })
    .then(function(result) { console.log('success: ' + result) })
    .catch(function(error) { console.error(error) } )
    ;

function delay(ms) {
    const promise = new Promise((resolve, reject) => {
        setTimeout(() => resolve(), ms);
    });
    return promise;
}

delay(1000).then(() => console.log(new Date())); 

async function runText(text, timeout, setValue) {
    let currentStr = '';
    for (const char of text) {
        currentStr += char;
        setValue(currentStr);
        await delay(timeout);
        console.log(1);
    }
}

async function runStrings(strings, charTimeout, stringSwitchTimeout, setValue) {
    while (true) {
        for (const str of strings) {
            await runText(str, charTimeout, setValue);
            await delay(stringSwitchTimeout);
        }
    }
}
const ads = [
    'Настраиваю крутую рекламу',
    'Backend разработчик, дата аналитик',
    'Делаю классные сайты и лэндинги',
];

console.log('finish', new Date());
// runStrings(ads, 50, 1000, console.log);