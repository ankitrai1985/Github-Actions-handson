package com.rai.ankit.HelloWorld;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestControll
public class GreetingController {

    @GetMapping("/greeting")
    public String greeting(@RequestParam(value = "name",defaultValue = "world") String name) {
        return "Hello, " + name + "!";
    }
}
