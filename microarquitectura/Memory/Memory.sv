module Memory (input logic clk,wboolean,swinit,
					 input logic [31:0] address,wdata,
					 output logic [31:0] rdata,
					 output logic GPIO,GPIOBoolean
);
						 
	logic [31:0] mapadress,ROMdata, RAMdata;
						 
	RAM ram( clk,wboolean, mapadress, wdata, RAMdata);
	ROM rom(mapadress, ROMdata);
	
	always_comb
		begin
			if (address >= 'd000 && address < 'd57600)
				begin
					mapadress = address;
					rdata = RAMdata;
					GPIO = 1'b0;
					GPIOBoolean = 1'b0;
				end
			else if (address == 'd57600)
				begin
					mapadress = 32'b0;
					rdata = {31'b0, swinit};
					GPIO = 1'b0;
					GPIOBoolean = 1'b0;
				end
			else if (address == 'd57601 && wboolean == 1'b1)
				begin
					GPIO = wdata[0];
					GPIOBoolean = 1'b1;
					mapadress = 32'b0;
					rdata = 32'b0;
				end
			else if (address >= 'd57602 && address < 'd57702)
				begin
					mapadress = address - 'd57602;
					rdata = ROMdata;
					GPIO = 1'b0;
					GPIOBoolean = 1'b0;
				end		
			else
				begin
					GPIO = 1'b0;
					GPIOBoolean = 1'b0;
					mapadress = 32'b0;
					rdata = 32'b0;
				end
		end
						 
endmodule 