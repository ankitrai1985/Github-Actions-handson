package com.rai.ankit.HelloWorld;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {

    @GetMapping("/greeting")
    public String Greeting(@RequestParam(value = "name",defaultValue = "world") String name) {
        return "Hello, " + name + "!";
    }
}
