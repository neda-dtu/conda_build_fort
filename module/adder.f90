
module Adder

use Types_mod
contains
function adder_func(a, b) result(out)

    implicit none

    !Inputs
    real(kind=SP), intent(in) :: a
    real(kind=SP), intent(in) :: b

    !Outputs
    real(kind=SP) :: out

    out = a + b

end function adder_func

end module Adder