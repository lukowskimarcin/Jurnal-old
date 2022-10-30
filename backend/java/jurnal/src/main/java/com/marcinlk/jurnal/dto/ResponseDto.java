package com.marcinlk.jurnal.dto;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.marcinlk.jurnal.model.User;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@RequiredArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
public class ResponseDto {
    private final String status;
    private final Object payload;
    private String errors;
}
