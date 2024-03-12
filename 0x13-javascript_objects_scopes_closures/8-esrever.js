#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight(function (lst, current) {
    lst.push(current);
    return lst;
  }, []);
};
