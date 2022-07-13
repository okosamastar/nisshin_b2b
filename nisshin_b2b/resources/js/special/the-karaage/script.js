// JavaScript Document

$(function () {

	/* scroll */
	$('.section-detail .next a[href^="#"]').click(function () {
		var speed = 1500;
		var href = $(this).attr("href");
		var target = $(href == "#" || href == "" ? 'html' : href);
		var position = target.offset().top;
		$("html, body").animate({ scrollTop: position}, speed, "easeOutQuint");
		return false;
	});
	/* scroll */


	/* toggle */
	if (matchMedia('(max-width: 768px)').matches) {
		$(".btn a").removeClass("modal");
		$(".block-info .btn").click(function(){
			var index = $('.block-info .btn').index(this);
			$(".block-info .btn a").eq(index).toggleClass("active");
			$(this).next().slideToggle('fast');
			return false;
		});
	}
	/* toggle */


	/* inview */
	//#section-main
	$('#section-main').css('opacity', 0);
	$('#section-main').on('inview', function (event, isInView) {
		if (isInView) {
			$(this).addClass('fadeIn');
			$(this).css('opacity', 1);
		}
	});

	//#section01
	$('#section01 .block-info h2,#section01 .block-info p,#section01 .block_moviethumb,#section01 .movieatt').css('opacity', 0);

	$('#section01 .block-info h2').on('inview', function (event, isInView) {
		if (isInView) {
			$(this).addClass('slideInLeft');
			$(this).css('opacity', 1);
		}
	});

	$('#section01 .block-info p').on('inview', function (event, isInView) {
		if (isInView) {
			$(this).addClass('slideInRight');
			$(this).css('opacity', 1);
		}
	});

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section01 .block_moviethumb').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('fadeInUp');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section02').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section01 .block_moviethumb').addClass('fadeInUp');
				$('#section01 .block_moviethumb').css('opacity', 1);
			}
		});
	}

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section01 .movieatt').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('fadeInUp');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section02').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section01 .movieatt').addClass('fadeInUp');
				$('#section01 .movieatt').css('opacity', 1);
			}
		});
	}

	//#section02
	$('#section02 h2,#section02 ul').css('opacity', 0);

	$('#section02 ul').on('inview', function (event, isInView) {
		if (isInView) {
			$('#section02 h2').addClass('fadeInDown');
			$('#section02 h2').css('opacity', 1);
		}
	});

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section02 ul').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('fadeInUp');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section03').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section02 ul').addClass('fadeInUp');
				$('#section02 ul').css('opacity', 1);
			}
		});
	}

	//#section03
	$('#section03 .new,#section03 .block_ex,#section03 .ph').css('opacity', 0);

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section03 .new').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('bounceIn');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section03 .block_ex').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section03 .new').addClass('bounceIn');
				$('#section03 .new').css('opacity', 1);
			}
		});
	}

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section03 .block_ex').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('slideInRight');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section03 .block_ex .read').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section03 .block_ex').addClass('slideInRight');
				$('#section03 .block_ex').css('opacity', 1);
			}
		});
	}

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section03 .ph').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('slideInLeft');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section03 .block_ex .read').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section03 .ph').addClass('slideInLeft');
				$('#section03 .ph').css('opacity', 1);
			}
		});
	}

	//#section_graph
	$('#section_graph p').css('opacity', 0);
	$('#section_graph p').on('inview', function (event, isInView) {
		if (isInView) {
			$(this).addClass('fadeInUp');
			$(this).css('opacity', 1);
		}
	});

	//#section04
	$('#section04 .new,#section04 .block_ex,#section04 .ph').css('opacity', 0);

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section04 .block_ex').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('slideInLeft');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section04 .block_ex .read').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section04 .block_ex').addClass('slideInLeft');
				$('#section04 .block_ex').css('opacity', 1);
			}
		});
	}

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section04 .ph').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('slideInRight');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section04 .block_ex .read').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section04 .ph').addClass('slideInRight');
				$('#section04 .ph').css('opacity', 1);
			}
		});
	}

	//#section05
	$('#section05 .new,#section05 .block_ex,#section05 .ph').css('opacity', 0);

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section05 .block_ex').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('slideInRight');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section05 .block_ex .read').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section05 .block_ex').addClass('slideInRight');
				$('#section05 .block_ex').css('opacity', 1);
			}
		});
	}

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section05 .ph').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('slideInLeft');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section05 .block_ex .read').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section05 .ph').addClass('slideInLeft');
				$('#section05 .ph').css('opacity', 1);
			}
		});
	}

	//#section06
	$('#section06 .new,#section06 .block_ex,#section06 .ph').css('opacity', 0);

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section06 .block_ex').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('slideInLeft');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section06 .block_ex .read').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section06 .block_ex').addClass('slideInLeft');
				$('#section06 .block_ex').css('opacity', 1);
			}
		});
	}

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section06 .ph').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('slideInRight');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section06 .block_ex .read').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section06 .ph').addClass('slideInRight');
				$('#section06 .ph').css('opacity', 1);
			}
		});
	}

	//#section07
	$('#section07 .etc,#section07 .block_etc01,#section07 .block_etc02').css('opacity', 0);

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section07 .etc').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('bounceIn');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section07 .block_etc01').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section07 .etc').addClass('bounceIn');
				$('#section07 .etc').css('opacity', 1);
			}
		});
	}

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section07 .block_etc01').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('slideInLeft');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section07 .block_etc01 h2').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section07 .block_etc01').addClass('slideInLeft');
				$('#section07 .block_etc01').css('opacity', 1);
			}
		});
	}

	if (matchMedia('(max-width: 768px)').matches) {
		$('#section07 .block_etc02').on('inview', function (event, isInView) {
			if (isInView) {
				$(this).addClass('slideInRight');
				$(this).css('opacity', 1);
			}
		});
	} else {
		$('#section07 .block_etc02 h2').on('inview', function (event, isInView) {
			if (isInView) {
				$('#section07 .block_etc02').addClass('slideInRight');
				$('#section07 .block_etc02').css('opacity', 1);
			}
		});
	}
	/* inview */


	/* thumb-pc */
	$('.thumb-pc').click(function () {
		$('.modaal-content-container').addClass("selected");
		$('.modaal-close').addClass("selected");
	});
	/* thumb-pc */


});
/* function */
