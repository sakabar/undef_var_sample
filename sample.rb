#coding: utf-8

#未定義の変数undefined_varがあるが、return_undefined_var()関数を使わなければエラーが発生しない
def return_undefined_var()
  return undefined_var
end

if true
  puts "Hello, true Ruby wolrd"
else
  #ここには来ない
  #return_undefined_var()は実行されないので、エラーも出ない
  puts "Hello, false Ruby wolrd"
end
