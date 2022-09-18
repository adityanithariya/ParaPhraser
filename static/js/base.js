document.getElementById("codearea").focus()
document.getElementById('codearea').addEventListener('keydown', function (e) {
  var start = this.selectionStart;
  var end = this.selectionEnd;
  if (e.key == 'Tab') {
    e.preventDefault();

    // set textarea value to: text before caret + tab + text after caret
    this.value = this.value.substring(0, start) +
      "\t" + this.value.substring(end);

    // put caret at right position again
    this.selectionStart = this.selectionEnd = start + 1;
  }
  if (e.code == "ShiftLeft" || e.code == "ShiftRight") {
    Form = document.getElementById("form");
  }
  if (e.code == "Enter") {
    // e.preventDefault();
    try {
      Form.submit()
    } catch (error) {}
  }
  if (e.key == '(') {
    e.preventDefault();

    this.value = this.value.substring(0, start) + "()" + this.value.substring(end);

    this.selectionStart = this.selectionEnd = start + 1;
  }
  if (e.key == '{') {
    e.preventDefault();

    this.value = this.value.substring(0, start) + "{}" + this.value.substring(end);

    this.selectionStart = this.selectionEnd = start + 1;
  }
  if (e.key == '"') {
    e.preventDefault();

    this.value = this.value.substring(0, start) + '""' + this.value.substring(end);

    this.selectionStart = this.selectionEnd = start + 1;
  }
  if (e.key == "'") {
    e.preventDefault();

    this.value = this.value.substring(0, start) + "''" + this.value.substring(end);

    this.selectionStart = this.selectionEnd = start + 1;
  }
  if (e.key == '[') {
    e.preventDefault();

    this.value = this.value.substring(0, start) + '[]' + this.value.substring(end);

    this.selectionStart = this.selectionEnd = start + 1;
  }
  if (e.key == 'Backspace') {
    if ((this.value.substring(start-1, end) == '{') && ( this.value.substring(start, end+1) == '}')) {
      e.preventDefault();
      this.value = this.value.substring(0, start-1) + this.value.substring(end+1);
      this.selectionStart = this.selectionEnd = start - 1;
    }
    if ((this.value.substring(start-1, end) == '"') && ( this.value.substring(start, end+1) == '"')) {
      e.preventDefault();
      this.value = this.value.substring(0, start-1) + this.value.substring(end+1);
      this.selectionStart = this.selectionEnd = start - 1;
    }
    if ((this.value.substring(start-1, end) == "'") && ( this.value.substring(start, end+1) == "'")) {
      e.preventDefault();
      this.value = this.value.substring(0, start-1) + this.value.substring(end+1);
      this.selectionStart = this.selectionEnd = start - 1;
    }
    if ((this.value.substring(start-1, end) == '[') && ( this.value.substring(start, end+1) == ']')) {
      e.preventDefault();
      this.value = this.value.substring(0, start-1) + this.value.substring(end+1);
      this.selectionStart = this.selectionEnd = start - 1;
    }
    if ((this.value.substring(start-1, end) == '(') && ( this.value.substring(start, end+1) == ')')) {
      e.preventDefault();
      this.value = this.value.substring(0, start-1) + this.value.substring(end+1);
      this.selectionStart = this.selectionEnd = start - 1;
    }
  }
});


// IDE
// let editor;

// window.onload = function() {
//     editor = ace.edit("codearea");
//     editor.setTheme("ace/theme/monokai");
//     editor.session.setMode("ace/mode/c_cpp");
// }

// function changeLanguage() {

//     let language = $("#languages").val();

//     if(language == 'c' || language == 'cpp')editor.session.setMode("ace/mode/c_cpp");
//     else if(language == 'php')editor.session.setMode("ace/mode/php");
//     else if(language == 'python')editor.session.setMode("ace/mode/python");
//     else if(language == 'node')editor.session.setMode("ace/mode/javascript");
// }
