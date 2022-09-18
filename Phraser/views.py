from django.shortcuts import render
from subprocess import check_output, CalledProcessError

def pyCompiler(request):
	if request.method == "GET":
		context = {
			"code": "",
			"output": ""
		}
		return render(request, "index.html", context=context)
	if request.method == "POST":
		with open("main.py", "w") as f:
			f.write(request.POST["code"])
		
		try:
			output = check_output(["python", "main.py"]).decode()
		except CalledProcessError as e:
			output = e.output

		context = {
			"code": request.POST["code"],
			"output": output,
		}
		return render(request, "index.html", context=context)

def cCompiler(request):
	if request.method == "GET":
		context = {
			"code": "#include <stdio.h>\n\nint main(){\n    \n    return 0;\n}\n",
			"output": ""
		}
		return render(request, "index.html", context=context)
	if request.method == "POST":
		with open("main.c", "w") as f:
			f.write(request.POST["code"])

		try:
			check_output(["gcc", "main.c", "-o", "main"])
			output = check_output(["./main.exe"]).decode()
		except CalledProcessError as e:
			output = e.output

		context = {
			"code": request.POST["code"],
			"output": output,
		}
		return render(request, "index.html", context=context)

def cppCompiler(request):
	if request.method == "GET":
		context = {
			"code": "#include <iostream>\nusing namespace std;\n\nint main(){\n    \n    return 0;\n}\n",
			"output": ""
		}
		return render(request, "index.html", context=context)
	if request.method == "POST":
		with open("main.cpp", "w") as f:
			f.write(request.POST["code"])

		try:
			check_output(["g++", "main.cpp", "-o", "main"])
			output = check_output(["./main.exe"]).decode()
		except CalledProcessError as e:
			output = e.output

		context = {
			"code": request.POST["code"],
			"output": output,
		}
		return render(request, "index.html", context=context)

def javaCompiler(request):
	if request.method == "GET":
		context = {
			"code": 'class Example{\n    public static void main(String[] args){\n        System.out.println("Hello World!");\n    }\n}\n',
			"output": "",
		}
		return render(request, "index.html", context=context)
	if request.method == "POST":
		className = request.POST["code"].split("main")[0].split("class ")[-1].split("{")[0]
		with open(className + ".java", "w") as f:
			f.write(request.POST["code"])
		
		try:
			check_output(["javac", className + ".java"])
			output = check_output(["java", className]).decode()
		except CalledProcessError as e:
			output = e.output


		context = {
			"code": request.POST["code"],
			"output": output,
		}
		return render(request, "index.html", context=context)

def jsCompiler(request):
	if request.method == "GET":
		context = {
			"code": 'console.log("Hello World!");',
			"output": "",
		}
		return render(request, "index.html", context=context)
	if request.method == "POST":
		with open("main.js", "w") as f:
			f.write(request.POST["code"])

		try:
			output = check_output(["node", "main.js"]).decode()
		except CalledProcessError as e:
			output = e.output

		context = {
			"code": request.POST["code"],
			"output": output,
		}
		return render(request, "index.html", context=context)

def rCompiler(request):
	if request.method == "GET":
		context = {
			"code": '"Hello, World!"',
			"output": "",
		}
		return render(request, "index.html", context=context)
	if request.method == "POST":
		with open("main.R", "w") as f:
			f.write(request.POST["code"])

		try:
			output = check_output(["Rscript", "main.R"]).decode()
			context = {
				"code": request.POST["code"],
				"output": output,
			}
			return render(request, "index.html", context=context)

		except CalledProcessError as e:
			output = e.output

		if type(output) != str:
			output = output.decode()

		context = {
			"code": request.POST["code"],
			"output": output,
		}
		return render(request, "index.html", context=context)

def goCompiler(request):
	if request.method == "GET":
		context = {
			"code": 'package main\nimport "fmt"\nfunc main() {\n    fmt.Println("hello world")\n}',
			"output": "",
		}
		return render(request, "index.html", context=context)
	if request.method == "POST":
		with open("main.go", "w") as f:
			f.write(request.POST["code"])

		try:
			output = check_output(["go", "run", "main.go"]).decode()
			context = {
				"code": request.POST["code"],
				"output": output,
			}
			return render(request, "index.html", context=context)

		except CalledProcessError as e:
			output = e.output

		context = {
			"code": request.POST["code"],
			"output": output,
		}
		return render(request, "index.html", context=context)

def rubyCompiler(request):
	if request.method == "GET":
		context = {
			"code": 'puts "Hello World!"',
			"output": "",
		}
		return render(request, "index.html", context=context)
	if request.method == "POST":
		with open("main.rb", "w") as f:
			f.write(request.POST["code"])

		try:
			output = check_output(["ruby", "main.rb"]).decode()
			context = {
				"code": request.POST["code"],
				"output": output,
			}
			return render(request, "index.html", context=context)

		except CalledProcessError as e:
			output = e.output

		context = {
			"code": request.POST["code"],
			"output": output,
		}
		return render(request, "index.html", context=context)
