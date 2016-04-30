#include "Interface.h"

#include <string>

// returns "hello, *name*, welcome on board!"
const char* greetings(char* name){
    std::string greetings = "Hello, " + std::string(name) + ", welcome onboard!";

    return greetings.c_str();
}


// performs an addition
float add(float number1, float number2){
    float result = number1 + number2;

    return result;
}


// perform a multiplication, the result is stored in the third argument
void multiply(float number1, float number2, float* result){
    *result = number1 * number2;
}
