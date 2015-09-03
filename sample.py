#coding: utf-8

#未定義の変数undefined_varがあるが、return_undefined_var()関数を使わなければエラーが発生しない
def return_undefined_var():
  return undefined_var

if True:
  print "Hello, true Python world!"
else:
  #ここには来ない
  #return_undefined_var()は実行されないので、エラーも出ない
  return_undefined_var()
  print "Hello, false Python world..."

#Python Tips:変数が定義されたかどうかを調べたい
#http://www.lifewithpython.com/2015/05/python-check-variable-existence.html
#これは変数ごとにいちいち調べなければいけない。実行時オプションなどで、コード中の全ての部分に未定義変数が含まれていないかどうか調べる方法はないのか?
