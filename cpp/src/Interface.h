#ifndef INTERFACE_H_
#define INTERFACE_H_

#include <iostream>

extern "C" {

    // returns "hello, *name*, welcome on board!"
    const char* greetings(char* name);

    // performs an addition
    float add(float number1, float number2);

    // perform a multiplication, the result is stored in the third argument
    void multiply(float number1, float number2, float* result);
}



#endif /* INTERFACE_H_ */
