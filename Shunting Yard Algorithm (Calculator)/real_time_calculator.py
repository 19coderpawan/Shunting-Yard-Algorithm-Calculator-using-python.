'''This is a Real time calculator where you just have to pass you arithmetic expression, and you will see the result .
for the logic I had used the Shunting Yard Algorithm which convert the infix to postfix expression which is very
secure and efficient algorithm for such task. And also for the fun part I had also used the text to speech window api
which I had accessed it using the python library called pywin32.'''

import win32com.client


# function to specify the precedence of the operator:
def precedence(operator):
    if operator in "+-":  # if operator == + or == -
        return 1
    elif operator in "*/":
        return 2
    else:
        return 0


# function to convert the infix exp to postfix exp.
def infix_to_postfix(infix_exp):
    stack = []  # it will handle the operator precedence
    output_queu = []  # it will hold the final postfix expression

    for token in infix_exp.split():
        if token.isdigit():  # this check if the token is a digit from 0 to 9.
            output_queu.append(int(token))  # this adds the digit by converting into the integer in the output_queue.

        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                # in this case you have to pop all the operators from the stack until you found the ( parentheses and
                # then finally discard that parentheses by poping out from the stack). this checks if the output_queue
                # is empty or not and the last element is accessed using the -1 index it a conviction to access the
                # last element from the stack in Shunting yard algorithm.
                output_queu.append(stack.pop())
            stack.pop()
        else:
            # print("current",token)
            while stack and precedence(stack[-1]) > precedence(token):
                output_queu.append(stack.pop())
            stack.append(token)
    while stack:
        output_queu.append(stack.pop())
    return output_queu


# function to evaluate the final postfix expression.
def postfix_exp_eval(postfix_exp):
    eval_stack = []  # this list is going to store the numbers which we are going to use for evaluation.
    for token in postfix_exp:
        if isinstance(token, int):  # check if the token is the instance of the class int .
            eval_stack.append(token)
        else:
            operand2 = eval_stack.pop()
            operand1 = eval_stack.pop()
            result = eval(f"{operand1} {token} {operand2}")  # Maintain order (left to right)
            eval_stack.append(result)
    print(eval_stack)


print("welcome to the robo calculator-:")
speak = win32com.client.Dispatch("SAPI.SpVoice")
speak.Speak("hello sir do you want to experience a fun way of calculating ")
speak.Speak("enter yes or no for further process")
choice = input("response-:")
if choice == "yes" or choice == "Yes":
    speak.Speak("Great choice Sir! I will not disappoint you!")
    speak.Speak(
        "please enter your expression and remember to place space after each tokens like 1 space + space 2 space + space 3")
    expression = input("enter your expression please use space like(1 + 2 + 3)-:")
    postfix = infix_to_postfix(expression)
    speak.Speak("Calculating---->")
    postfix_exp_eval(postfix)
    speak.Speak("Your result is on the screen !")
else:
    speak.Speak("Thanks for your time sir, but i must tell you you have missed a great experience ")
    speak.Speak("But what to say! it's your choice! see you soon sir.")

# imp points

'''
1.Using eval with untrusted user input is highly insecure and should be avoided.
2.The controlled use of eval within the Shunting-Yard algorithm, where the expression format is restricted and no external
code injection is possible, poses a lower security risk.

'''
