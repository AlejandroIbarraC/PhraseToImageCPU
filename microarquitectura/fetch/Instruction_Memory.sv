module Instruction_Memory(input logic [31:0] pc,
								  output logic [31:0] rdata
);
	// synthesis translate_off
	
	logic [31:0] Instructiondata[877:0];
	
	
	initial begin
	$readmemh("output.txt",Instructiondata);
	end
	
	
	assign rdata = Instructiondata[pc[31:0]];
	
	
		// synthesis translate_on
endmodule 