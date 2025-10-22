DAY,_,_ = __FILE__.rpartition(?.)


r=[]

File.open("#{DAY}.in", "r") { |f|
  f.each_line {|l|
    i = l.to_i
    r<<i
  }
}

_,*r=r
File.open("#{DAY}.out", "w") { |f|
r.map{|i|
  l=(3..i**0.5).filter{i%_1<1 || (i-1)%_1<1}+[i-1]
  x = i==2 ? -1 : i<4 ? i : l.find{i.digits(_1).max<=1}
  f.puts x
}
}
