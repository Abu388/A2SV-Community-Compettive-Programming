type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    console.log(promise1)
    const p1 = await promise1 
    const p2 = await promise2
    return p1 + p2
    // return promise1 + promise2
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */