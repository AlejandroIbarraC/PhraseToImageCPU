module MEM(input logic clk, memwBoolean, MemrBoolean, swinit,
			  input logic [31:0] A,ALUResult,
			  output logic GPIO,GPIOBoolean,
			  output logic [31:0] FinalResult
);

logic [31:0] Memrdata;

Memory memory_module(clk,memwBoolean,swinit,
								 A,ALUResult,
								 Memrdata,
								 GPIO,GPIOBoolean);
								 
Mux2_1 #(32) result_select(ALUResult, Memrdata, MemrBoolean , FinalResult);


endmodule 