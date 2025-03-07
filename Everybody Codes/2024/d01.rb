DAY,_,_ = __FILE__.rpartition(?.)

t=''

File.open("#{DAY}a.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp
    t+=l
  }
}

p t.count(?B)+t.count(?C)*3

# -----------------------

t=''
File.open("#{DAY}b.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp
    t+=l
  }
}

s=0
d={?A=>0, ?B=>1, ?C=>3, ?D=>5}
t.chars.each_slice(2).sum{
  x,y=d[_1],d[_2]
  x&&y && (x+=1;y+=1)
  s+=(x||0)+(y||0)
}

p s

# -----------------------

t=''
File.open("#{DAY}c.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp
    t+=l
  }
}

s=0
d={?A=>0, ?B=>1, ?C=>3, ?D=>5}
n={0=>0,1=>0,2=>2,3=>6}
t.chars.each_slice(3).sum{
  x,y,z=d[_1],d[_2],d[_3]
  s+=(x||0)+(y||0)+(z||0) + ( n[[x,y,z].count{|i|i}])
}

p s