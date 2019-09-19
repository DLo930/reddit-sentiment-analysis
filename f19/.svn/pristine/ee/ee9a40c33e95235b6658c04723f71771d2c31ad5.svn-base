/* Debugging with contracts; simulating cc0 -d
 * Enable with gcc -DDEBUG ...
 *
 * 15-122 Principles of Imperative Computation
 * Frank Pfenning
 */

#include <assert.h>
#include <setjmp.h>

/* Unlike typical header files, "contracts.h" may be
 * included multiple times, with and without DEBUG defined.
 * For this to succeed we first undefine the macros in
 * question in order to avoid a redefinition warning.
 */

#undef FAIL

#undef ASSERT
#undef REQUIRES
#undef ENSURES

#ifdef DEBUG_FAIL

/* define DEBUG so that #ifdef DEBUG ... #endif works */
#define DEBUG 1

/* Global jump buffer to use on contract failure */
jmp_buf _contracts_env_;
int _failed_contracts_;

#define FAIL(e) ((setjmp(_contracts_env_) == 0) ? (void)(e) : (void)_failed_contracts_++)
#define FAILURES _failed_contracts_
#define FAILURES_RESET() ((void)(_failed_contracts_ = 0))

#define ASSERT(e) ((e) ? (void)0 : longjmp(_contracts_env_, 1))
#define REQUIRES(e) ((e) ? (void)0 : longjmp(_contracts_env_, 2))
#define ENSURES(e) ((e) ? (void)0 : longjmp(_contracts_env_, 3))

#else

#define FAIL(COND) ((void)0)
#define FAILURES 0
#define FAILURES_RESET ((void)0)

#ifdef DEBUG

#define ASSERT(COND) assert(COND)
#define REQUIRES(COND) assert(COND)
#define ENSURES(COND) assert(COND)

#else

#define FAIL(COND) ((void)0)

#define ASSERT(COND) ((void)0)
#define REQUIRES(COND) ((void)0)
#define ENSURES(COND) ((void)0)

#endif
#endif
