module Extender_test();
	logic [26:0] Instr;
	logic [1:0] immediatetype;
	logic [31:0] extendeddata;
	
	Extender uut (Instr,immediatetype, extendeddata);
	
	initial begin
	//Prueba case 1
	immediatetype = 2'b00;
	Instr = 27'd1;
	#10;
	
	assert ( extendeddata === 31'd0) $display("El caso termina satisfactoriamente"); else $display("Hay algun error");
	
	//Prueba case 2
	immediatetype = 2'b01;
	Instr = 27'd1;
	#10;
	
	assert ( extendeddata === 31'd1) $display("El caso termina satisfactoriamente"); else $display("Hay algun error");
	
	//Prueba case 3
	immediatetype = 2'b10;
	Instr = 27'd0;
	#10;
	
	assert ( extendeddata === 31'd0) $display("El caso termina satisfactoriamente"); else $display("Hay algun error");
	
	//Prueba case 4
	immediatetype = 2'b11;
	Instr = 27'd1;
	#10;
	
	assert ( extendeddata === 31'd1) $display("El caso termina satisfactoriamente"); else $display("Hay algun error");
end
endmodule
