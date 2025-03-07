DAY,_,_ = __FILE__.rpartition(?.)

require'prime'
require'z3'

r=[]

File.open("#{DAY}a.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp    
    r+=[l]
  }
}

a,_,s=r

a=a[6..].split(/,/)
p s.scan(/(?=#{a*?|})/).size


# -----------------------


r=[]

File.open("#{DAY}b.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp
    r+=[l]
  }
}

a,_,*l=r

a=a[6..].split(/,/)
a+=a.map(&:reverse)
p l.sum{|s|
  x=' '*s.size
  a.map{|w|
    s.scan(/(?=#{w})/){v=w.size;x[$`.size,v]='.'*v}
  }
  x.count(?.)
}

# -----------------------

r=[]

File.open("#{DAY}c.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp
    r+=[l]
    
  }
}

a,_,*l=r

a=a[6..].split(/,/)
a+=a.map(&:reverse)

W,H=l.size,l[0].size

l=l.map{_1*3}
m=l.map{' '*_1.size}
2.times{
  m=l.zip(m).map{|s,x|
    a.map{|w|
      s.scan(/(?=#{w})/){v=w.size;x[$`.size,v]='.'*v}
    }
    x
  }
  l=l.map(&:chars).transpose.map{_1*''}
  m=m.map(&:chars).transpose.map{_1*""}
}
m=m.map{_1[H,H]}
p m.sum{_1.count ?.}