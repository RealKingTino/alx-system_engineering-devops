#!/usr/bin/env ruby

if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit 1
end

input_string = ARGV[0]

regex = /School/

matches = input_string.scan(regex)

result = matches.join

puts result
