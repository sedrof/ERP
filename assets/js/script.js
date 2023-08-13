async function openPythonFile(filename) {
    await eel.open_python_file(filename)();
}