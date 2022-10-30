package com.marcinlk.jurnal.service;

import org.springframework.stereotype.Service;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor // uzywanie konstruktora z arugmentami dla latwiejszego testowanie przez testy
                         // jednostkow (latwo dac mocki)
public class CandleServiceImpl implements CandleService {

    // private final CandleRepository candleRepository;
}
