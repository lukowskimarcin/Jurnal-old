package com.marcinlk.jurnal.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.marcinlk.jurnal.exception.InvalidUserException;
import com.marcinlk.jurnal.model.User;

import lombok.extern.slf4j.Slf4j;

@RestController
@Slf4j
@RequestMapping("api/v1")
public class HelloController {
    // private static final Logger logger =
    // LoggerFactory.getLogger(HelloController.class);

    @GetMapping("/hello")
    public ResponseEntity<List<User>> sayHello() {
        log.info("test loggera");

        // throw new InvalidUserException("message2");
        User u = new User(1, "2", "3", "4");

        List<User> x = new ArrayList<>();
        x.add(u);
        x.add(u);
        x.add(u);

        return new ResponseEntity<List<User>>(x, HttpStatus.OK);
    }

    @ExceptionHandler(value = InvalidUserException.class)
    public ResponseEntity<String> handleInvalidUserException(InvalidUserException ex) {
        log.error("Error", ex);
        return new ResponseEntity<String>("Invalid user exception occurs: " + ex.getMessage(),
                HttpStatus.INTERNAL_SERVER_ERROR);
    }
}
