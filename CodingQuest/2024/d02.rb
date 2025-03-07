DAY,_,_ = __FILE__.rpartition(?.)

require'prime'
require'z3'

r=[]
t=''
s=0
a=b=0

File.open("#{DAY}.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp
    #l=l.scan(/-?\d+/).map &:to_i
    #l=l.split.map &:to_i
    #l=l.chars.map &:to_i
    #l=l.split
    #l=l.to_i
    #l=l.chars

    s=l[4,4].to_i 16
    i = l[24,4].to_i 16
    j = l[32,4].to_i 16
    (i == 10*256 || j==10*256) && (b+=s) 
    (i == 192*256+168 || j==192*256+168) && (a+=s)
  }
}

puts [a,b]*?/