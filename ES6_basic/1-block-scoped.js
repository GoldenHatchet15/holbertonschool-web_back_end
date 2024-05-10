export default function taskBlock(trueOrFalse) {
  const initialTask = false;
  const initialTask2 = true;
  const resultTask = trueOrFalse ? true : initialTask;
  const resultTask2 = trueOrFalse ? false : initialTask2;

  return [resultTask, resultTask2];
}
