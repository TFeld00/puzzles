DAY,_,_ = __FILE__.rpartition(?.)

require'prime'
require'z3'

r=[]
t=''
s=0

File.open("#{DAY}.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp
    #l=l.scan(/-?\d+/).map &:to_i
    #l=l.split.map &:to_i
    #l=l.chars.map &:to_i
    #l=l.split
    #l=l.to_i
    #l=l.chars
    
    t+=l
  }
}

l=''
i=0
t.split.map{l+='.#'[i^=1]*_1.to_i}
puts l.chars.each_slice(100).map{_1*''}