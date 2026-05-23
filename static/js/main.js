/**
 * 水书仪式信息可视化 — 片头动画 & 交互热区 & 弹窗
 */

(function () {
    "use strict";

    /* ==================== 片头动画 ==================== */
    const wrap = document.getElementById("mainWrap");
    if (wrap) {
        // 1. 开场：图片虚化 + 遮罩出现
        wrap.classList.add("intro");

        // 2. 0.3s 后文字浮入
        setTimeout(function () {
            wrap.classList.add("show-text");
        }, 300);

        // 3. 2.8s 后虚化消散，文字保留
        setTimeout(function () {
            wrap.classList.remove("intro");
        }, 2800);

        // 4. 3.2s 后激活播放圆点 + 香炉烟雾
        setTimeout(function () {
            var dot = document.getElementById("playDot");
            if (dot) dot.classList.add("active");
            var smoke = document.getElementById("incenseSmoke");
            if (smoke) smoke.classList.add("smoke-on");
        }, 3200);
    }

    /* ==================== 视频弹窗 ==================== */
    var playDot = document.getElementById("playDot");
    var videoOverlay = document.getElementById("videoOverlay");
    var videoEl = document.getElementById("mainVideo");
    var videoClose = document.getElementById("videoClose");
    var watched = false;

    function openVideo() {
        videoOverlay.classList.add("show");
        if (videoEl) {
            videoEl.currentTime = 0;
            videoEl.play();
        }
        if (!watched) {
            watched = true;
            playDot.classList.add("watched");
        }
    }

    function closeVideo() {
        videoOverlay.classList.remove("show");
        if (videoEl) {
            videoEl.pause();
        }
    }

    if (playDot && videoOverlay) {
        playDot.addEventListener("click", function (e) {
            e.stopPropagation();
            openVideo();
        });

        if (videoClose) {
            videoClose.addEventListener("click", closeVideo);
        }

        videoOverlay.addEventListener("click", function (e) {
            if (e.target === videoOverlay) closeVideo();
        });
    }

    /* ==================== 标签切换 ==================== */
    var tabBtns = document.querySelectorAll(".tab-btn");
    tabBtns.forEach(function (btn) {
        btn.addEventListener("click", function () {
            var pageId = btn.getAttribute("data-page");
            tabBtns.forEach(function (b) { b.classList.remove("active"); });
            btn.classList.add("active");
            document.querySelectorAll(".page").forEach(function (p) {
                p.classList.remove("active");
            });
            var target = document.getElementById(pageId);
            if (target) target.classList.add("active");
            if (pageId === "page3") {
                setTimeout(function () {
                    var dom = document.getElementById("sankeyChart");
                    if (dom) {
                        var instance = echarts.getInstanceByDom(dom);
                        if (instance) instance.resize();
                    }
                }, 100);
            }
        });
    });

    /* ==================== 端节场景弹窗 ==================== */
    var duanJieBox = document.querySelector('[data-tip="端节-序"]');
    var sceneOverlayEl = document.getElementById("sceneOverlay");
    var sceneCloseBtn = document.getElementById("sceneClose");
    var sceneBgm = document.getElementById("sceneBgm");

    function openScene() {
        sceneOverlayEl.classList.add("show");
        if (sceneBgm) {
            sceneBgm.currentTime = 0;
            sceneBgm.play().catch(function () {});
        }
    }

    function closeScene() {
        sceneOverlayEl.classList.remove("show");
        if (sceneBgm) {
            sceneBgm.pause();
            sceneBgm.currentTime = 0;
        }
    }

    if (duanJieBox && sceneOverlayEl) {
        duanJieBox.addEventListener("click", function (e) {
            e.stopPropagation();
            openScene();
        });

        if (sceneCloseBtn) {
            sceneCloseBtn.addEventListener("click", closeScene);
        }

        sceneOverlayEl.addEventListener("click", function (e) {
            if (e.target === sceneOverlayEl) {
                closeScene();
            }
        });
    }

    /* ==================== 元素详情弹窗 ==================== */
    var elemCards = document.querySelectorAll(".card-elem");
    var elemOverlay = document.getElementById("elemDetailOverlay");
    var elemCloseBtn = document.getElementById("elemDetailClose");
    var elemImg = document.getElementById("elemDetailImg");
    var elemCaption = document.getElementById("elemDetailCaption");

    if (elemCards.length && elemOverlay && window.elemDetailImages && window.elemDetailImages.length) {
        elemCards.forEach(function (card) {
            card.addEventListener("click", function () {
                var idx = parseInt(card.getAttribute("data-elem"), 10);
                if (elemImg && window.elemDetailImages[idx]) {
                    var mime = (window.elemDetailMimes && window.elemDetailMimes[idx]) || 'image/png';
                    elemImg.src = "data:" + mime + ";base64," + window.elemDetailImages[idx];
                }
                if (elemCaption && window.elemDetailCaptions && window.elemDetailCaptions[idx]) {
                    elemCaption.textContent = window.elemDetailCaptions[idx];
                }
                elemOverlay.classList.add("show");
            });
        });

        if (elemCloseBtn) {
            elemCloseBtn.addEventListener("click", function () {
                elemOverlay.classList.remove("show");
            });
        }

        elemOverlay.addEventListener("click", function (e) {
            if (e.target === elemOverlay) {
                elemOverlay.classList.remove("show");
            }
        });
    }

    /* ==================== 全局 Escape ==================== */
    document.addEventListener("keydown", function (e) {
        if (e.key !== "Escape") return;
        if (elemOverlay && elemOverlay.classList.contains("show")) {
            elemOverlay.classList.remove("show");
            return;
        }
        if (sceneOverlayEl && sceneOverlayEl.classList.contains("show")) {
            closeScene();
            return;
        }
        if (videoOverlay && videoOverlay.classList.contains("show")) {
            closeVideo();
        }
    });

    /* ==================== 交互热区 ==================== */
    const boxes = document.querySelectorAll(".hot-box");
    const tooltip = document.getElementById("tooltip");

    if (!wrap) return;
    if (!boxes.length || !tooltip) return;

    let activeBox = null;

    function showTooltip(box, event) {
        const text = box.getAttribute("data-tip");
        tooltip.textContent = text;
        tooltip.style.display = "block";
        moveTooltip(event);
    }

    function moveTooltip(event) {
        if (!activeBox) return;
        const rect = wrap.getBoundingClientRect();
        const tooltipW = tooltip.offsetWidth;
        const gap = 16;
        let x = event.clientX - rect.left + gap;
        let y = event.clientY - rect.top + gap;

        // 右侧超出则向左弹出
        if (x + tooltipW > rect.width) {
            x = event.clientX - rect.left - tooltipW - gap;
        }
        // 下方超出则向上弹出
        const tooltipH = tooltip.offsetHeight;
        if (y + tooltipH > rect.height) {
            y = event.clientY - rect.top - tooltipH - gap;
        }

        tooltip.style.left = x + "px";
        tooltip.style.top = y + "px";
    }

    function hideTooltip() {
        tooltip.style.display = "none";
        activeBox = null;
    }

    boxes.forEach(function (box) {
        box.addEventListener("mouseenter", function (e) {
            activeBox = box;
            showTooltip(box, e);
        });

        box.addEventListener("mouseleave", function () {
            hideTooltip();
        });

        /* 移动端触摸适配 */
        box.addEventListener("touchstart", function (e) {
            activeBox = box;
            showTooltip(box, e.touches[0]);
        }, { passive: true });

        box.addEventListener("touchend", function () {
            setTimeout(hideTooltip, 800);
        });
    });

    // 在 wrapper 上监听 mousemove，保证在热区之间移动时弹窗跟随流畅
    wrap.addEventListener("mousemove", function (e) {
        if (activeBox) {
            moveTooltip(e);
        }
    });

    // 离开整个 wrapper 时也隐藏
    wrap.addEventListener("mouseleave", function () {
        hideTooltip();
    });
})();
