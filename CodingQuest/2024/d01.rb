DAY,_,_ = __FILE__.rpartition(?.)

require'prime'
require'z3'

r=[]
t=''
s=0
d={}

File.open("#{DAY}.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp
    #l=l.scan(/-?\d+/).map &:to_i
    #l=l.split.map &:to_i
    #l=l.chars.map &:to_i
    a,b,c=l.split
    #l=l.to_i
    #l=l.chars
    
    d[a]||=0
    d[a] += c.to_i * (b[/Rebate|Discount/] ? -1 : 1)
    
  }
}

p d.values.min
