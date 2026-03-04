DAY,_,_ = __FILE__.rpartition(?.)

require'prime'
require'z3'

r=[]
t=''
s=0

File.open("#{DAY}a.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp
    #l=l.scan(/-?\d+/).map &:to_i
    #l=l.split.map &:to_i
    #l=l.chars.map &:to_i
    #l=l.split
    #l=l.to_i
    #l=l.chars
    
    r+=[l]
    t+=l
  }
}

p r
p t