 module flag_cero #(parameter N = 4)(input logic [N-1:0] result,
												 input logic f_carry,
												 output logic flag );
										
assign flag = (result=='b0) & (f_carry==1'b0);

endmodule 