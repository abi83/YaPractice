const delay = (ms: number) => new Promise<void>(resolve => setTimeout(resolve, ms));

function makeAsyncLoop<T>(run: (data: T) => Promise<void>) {
    return async (data: T) => {
        while (true) {
            await run(data);
        }
    }
}

function makeMultiRunner<T>(processValue: (value: T) => Promise<void>, timeout: number) {
    return async (values: T[]) => {
        for (const val of values) {
            await processValue(val);
            await delay(timeout);
        }
    }
} 

function makeTextRunner(setValue: (value: string) => void, timeout: number) {
    return async (text: string) => {
        let currentStr = '';
        for (const char of text) {
            currentStr += char;
            setValue(currentStr);
            await delay(timeout)
        }
    }
}

function print(text: string){
    process.stdout.clearLine(0);
    process.stdout.cursorTo(0);
    process.stdout.write(text);
}

const runLine = makeTextRunner(print, 50);
const runLines = makeMultiRunner(runLine, 1000);
const runLinesForever = makeAsyncLoop(runLines);

const ads = [
    'Настраиваю крутую рекламу',
    'Backend разработчик, дата аналитик',
    'Делаю классные сайты и лэндинги',
];

// runLine(ads[0]);
// runLines(ads);
runLinesForever(ads);