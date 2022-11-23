package com.marcinlk.jurnal.dto;

import lombok.Data;

@Data
public class RateDTO {
    private Long time;
    private Double open;
    private Double high;
    private Double low;
    private Double close;
    private Long tickVolume;
    private Long spread;
    private Long realVolume;
}
