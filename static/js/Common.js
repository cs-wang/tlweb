function IsMobile(tel) {
    var reg = /^0?1[3|4|5|7|8][0-9]\d{8}$/;
    if (reg.test(tel)) {
        return true;
    } else {
        return false;
    };
}



var Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1];    // 加权因子   
var ValideCode = [1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2];            // 身份证验证位值.10代表X   
function IdCardValidate(idCard) {
    idCard = trim(idCard.replace(/ /g, ""));               //去掉字符串头尾空格                     
    if (idCard.length == 15) {
        return isValidityBrithBy15IdCard(idCard);       //进行15位身份证的验证    
    } else if (idCard.length == 18) {
        var a_idCard = idCard.split("");                // 得到身份证数组   
        if (isValidityBrithBy18IdCard(idCard) && isTrueValidateCodeBy18IdCard(a_idCard)) {   //进行18位身份证的基本验证和第18位的验证
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}
/**  
 * 判断身份证号码为18位时最后的验证位是否正确  
 * @param a_idCard 身份证号码数组  
 * @return  
 */
function isTrueValidateCodeBy18IdCard(a_idCard) {
    var sum = 0;                             // 声明加权求和变量   
    if (a_idCard[17].toLowerCase() == 'x') {
        a_idCard[17] = 10;                    // 将最后位为x的验证码替换为10方便后续操作   
    }
    for (var i = 0; i < 17; i++) {
        sum += Wi[i] * a_idCard[i];            // 加权求和   
    }
    valCodePosition = sum % 11;                // 得到验证码所位置   
    if (a_idCard[17] == ValideCode[valCodePosition]) {
        return true;
    } else {
        return false;
    }
}
/**  
  * 验证18位数身份证号码中的生日是否是有效生日  
  * @param idCard 18位书身份证字符串  
  * @return  
  */
function isValidityBrithBy18IdCard(idCard18) {
    var year = idCard18.substring(6, 10);
    var month = idCard18.substring(10, 12);
    var day = idCard18.substring(12, 14);
    var temp_date = new Date(year, parseFloat(month) - 1, parseFloat(day));
    // 这里用getFullYear()获取年份，避免千年虫问题   
    if (temp_date.getFullYear() != parseFloat(year)
          || temp_date.getMonth() != parseFloat(month) - 1
          || temp_date.getDate() != parseFloat(day)) {
        return false;
    } else {
        return true;
    }
}
/**  
 * 验证15位数身份证号码中的生日是否是有效生日  
 * @param idCard15 15位书身份证字符串  
 * @return  
 */
function isValidityBrithBy15IdCard(idCard15) {
    var year = idCard15.substring(6, 8);
    var month = idCard15.substring(8, 10);
    var day = idCard15.substring(10, 12);
    var temp_date = new Date(year, parseFloat(month) - 1, parseFloat(day));
    // 对于老身份证中的你年龄则不需考虑千年虫问题而使用getYear()方法   
    if (temp_date.getYear() != parseFloat(year)
            || temp_date.getMonth() != parseFloat(month) - 1
            || temp_date.getDate() != parseFloat(day)) {
        return false;
    } else {
        return true;
    }
}
//去掉字符串头尾空格   
function trim(str) {
    return str.replace(/(^\s*)|(\s*$)/g, "");
}
String.prototype.replaceAll = function (reallyDo, replaceWith, ignoreCase) {
    if (!RegExp.prototype.isPrototypeOf(reallyDo)) {
        return this.replace(new RegExp(reallyDo, (ignoreCase ? "gi" : "g")), replaceWith);
    } else {
        return this.replace(reallyDo, replaceWith);
    }
}

function IsBankName(s)
{

}


//bankno为银行卡号 banknoInfo为显示提示信息的DIV或其他控件
function IsBankNo(bankno) {
    var lastNum = bankno.substr(bankno.length - 1, 1);//取出最后一位（与luhm进行比较）

    var first15Num = bankno.substr(0, bankno.length - 1);//前15或18位
    var newArr = new Array();
    for (var i = first15Num.length - 1; i > -1; i--) {    //前15或18位倒序存进数组
        newArr.push(first15Num.substr(i, 1));
    }
    var arrJiShu = new Array();  //奇数位*2的积 <9
    var arrJiShu2 = new Array(); //奇数位*2的积 >9

    var arrOuShu = new Array();  //偶数位数组
    for (var j = 0; j < newArr.length; j++) {
        if ((j + 1) % 2 == 1) {//奇数位
            if (parseInt(newArr[j]) * 2 < 9)
                arrJiShu.push(parseInt(newArr[j]) * 2);
            else
                arrJiShu2.push(parseInt(newArr[j]) * 2);
        }
        else //偶数位
            arrOuShu.push(newArr[j]);
    }

    var jishu_child1 = new Array();//奇数位*2 >9 的分割之后的数组个位数
    var jishu_child2 = new Array();//奇数位*2 >9 的分割之后的数组十位数
    for (var h = 0; h < arrJiShu2.length; h++) {
        jishu_child1.push(parseInt(arrJiShu2[h]) % 10);
        jishu_child2.push(parseInt(arrJiShu2[h]) / 10);
    }

    var sumJiShu = 0; //奇数位*2 < 9 的数组之和
    var sumOuShu = 0; //偶数位数组之和
    var sumJiShuChild1 = 0; //奇数位*2 >9 的分割之后的数组个位数之和
    var sumJiShuChild2 = 0; //奇数位*2 >9 的分割之后的数组十位数之和
    var sumTotal = 0;
    for (var m = 0; m < arrJiShu.length; m++) {
        sumJiShu = sumJiShu + parseInt(arrJiShu[m]);
    }

    for (var n = 0; n < arrOuShu.length; n++) {
        sumOuShu = sumOuShu + parseInt(arrOuShu[n]);
    }

    for (var p = 0; p < jishu_child1.length; p++) {
        sumJiShuChild1 = sumJiShuChild1 + parseInt(jishu_child1[p]);
        sumJiShuChild2 = sumJiShuChild2 + parseInt(jishu_child2[p]);
    }
    //计算总和
    sumTotal = parseInt(sumJiShu) + parseInt(sumOuShu) + parseInt(sumJiShuChild1) + parseInt(sumJiShuChild2);

    //计算Luhm值
    var k = parseInt(sumTotal) % 10 == 0 ? 10 : parseInt(sumTotal) % 10;
    var luhm = 10 - k;

    if (lastNum == luhm && lastNum.length != 0) {
        return true;
    }
    else {
        return false;
    }
}

function formatBankNo(BankNo) {
    if (BankNo.value == "") return;
    var account = new String(BankNo.value);
    account = account.substring(0, 22); /*帐号的总数, 包括空格在内 */
    if (account.match(".[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{7}") == null) {
        /* 对照格式 */
        if (account.match(".[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{7}|" + ".[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{7}|" +
        ".[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{7}|" + ".[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{7}") == null) {
            var accountNumeric = accountChar = "", i;
            for (i = 0; i < account.length; i++) {
                accountChar = account.substr(i, 1);
                if (!isNaN(accountChar) && (accountChar != " ")) accountNumeric = accountNumeric + accountChar;
            }
            account = "";
            for (i = 0; i < accountNumeric.length; i++) {    /* 可将以下空格改为-,效果也不错 */
                if (i == 4) account = account + " "; /* 帐号第四位数后加空格 */
                if (i == 8) account = account + " "; /* 帐号第八位数后加空格 */
                if (i == 12) account = account + " ";/* 帐号第十二位后数后加空格 */
                account = account + accountNumeric.substr(i, 1)
            }
        }
    }
    else {
        account = " " + account.substring(1, 5) + " " + account.substring(6, 10) + " " + account.substring(14, 18) + "-" + account.substring(18, 25);
    }
    if (account != BankNo.value) BankNo.value = account;
}





function TextMagnifier(options) {

    this.config = {

        inputElem: '.inputElem',     // 输入框目标元素
        parentCls: '.parentCls',     // 目标元素的父类
        align: 'right',            // 对齐方式有 ['top','bottom','left','right']四种 默认为top
        splitType: [3, 4, 4],          // 拆分规则
        delimiter: ' '                // 分隔符可自定义
    };

    this.cache = {
        isFlag: false
    };
    this.init(options);
}

TextMagnifier.prototype = {

    constructor: TextMagnifier,

    init: function (options) {
        this.config = $.extend(this.config, options || {});
        var self = this,
			_config = self.config,
			_cache = self.cache;

        self._bindEnv();


    },
    /*
     * 在body后动态添加HTML内容
     * @method _appendHTML
     */
    _appendHTML: function ($this, value) {
        var self = this,
            _config = self.config,
            _cache = self.cache;

        var html = '',
            $parent = $($this).closest(_config.parentCls);

        if ($('.js-max-input', $parent).length == 0) {
            html += '<div class="js-max-input"></div>';
            $($parent).append(html);
        }
        var value = self._formatStr(value);
        $('.js-max-input', $parent).html(value);
    },
    /*
     * 给目标元素定位
     * @method _position
     * @param target
     */
    _position: function (target) {
        var self = this,
			_config = self.config;
        var elemWidth = $(target).outerWidth(),
			elemHeight = $(target).outerHeight(),
			elemParent = $(target).closest(_config.parentCls),
			containerHeight = $('.js-max-input', elemParent).outerHeight();

        $(elemParent).css({ "position": 'relative' });

        switch (true) {

            case _config.align == 'top':

                $('.js-max-input', elemParent).css({ 'position': 'absolute', 'top': -elemHeight - containerHeight / 2, 'left': 0 });
                break;

            case _config.align == 'left':

                $('.js-max-input', elemParent).css({ 'position': 'absolute', 'top': 0, 'left': 0 });
                break;

            case _config.align == 'bottom':

                $('.js-max-input', elemParent).css({ 'position': 'absolute', 'top': elemHeight + 4 + 'px', 'left': 0 });
                break;

            case _config.align == 'right':

                $('.js-max-input', elemParent).css({ 'position': 'absolute', 'top': 0, 'left': elemWidth + 2 + 'px' });
                break;
        }
    },
    /**
     * 绑定事件
     * @method _bindEnv
     */
    _bindEnv: function () {
        var self = this,
			_config = self.config,
			_cache = self.cache;

        // 实时监听输入框值的变化
        $(_config.inputElem).each(function (index, item) {

            $(item).keyup(function (e) {
                var value = $.trim(e.target.value),
					parent = $(this).closest(_config.parentCls);
                if (value == '') {
                    self._hide(parent);
                } else {

                    var html = $.trim($('.js-max-input', parent).html());

                    if (html != '') {
                        self._show(parent);
                    }
                }
                self._appendHTML($(this), value);
                self._position($(this));
            });

            $(item).unbind('focusin');
            $(item).bind('focusin', function () {
                var parent = $(this).closest(_config.parentCls),
					html = $.trim($('.js-max-input', parent).html());

                if (html != '') {
                    self._show(parent);
                }
            });

            $(item).unbind('focusout');
            $(item).bind('focusout', function () {
                var parent = $(this).closest(_config.parentCls);
                self._hide(parent);
            });
        });
    },
    /**
     * 格式化下
     * @method _formatStr
     */
    _formatStr: function (str) {
        var self = this,
			_config = self.config,
			_cache = self.cache;
        var count = 0,
			output = [];
        for (var i = 0, ilen = _config.splitType.length; i < ilen; i++) {
            var s = str.substr(count, _config.splitType[i]);
            if (s.length > 0) {
                output.push(s);
            }
            count += _config.splitType[i];
        }
        return output.join(_config.delimiter);
    },
    /*
     * 显示 放大容器
     * @method _show
     */
    _show: function (parent) {
        var self = this,
			_config = self.config,
			_cache = self.cache;
        if (!_cache.isFlag) {
            $('.js-max-input', parent).show();
            _cache.isFlag = true;
        }
    },
    /*
     * 隐藏 放大容器
     * @method hide
     * {public}
     */
    _hide: function (parent) {
        var self = this,
			_config = self.config,
			_cache = self.cache;
        if (_cache.isFlag) {
            $('.js-max-input', parent).hide();
            _cache.isFlag = false;
        }
    }
};



function formatStr(str, splitType, delimiter) {
    var count = 0,
        output = [];
    for (var i = 0, ilen = splitType.length; i < ilen; i++) {
        var s = str.substr(count, splitType[i]);
        if (s.length > 0) {
            output.push(s);
        }
        count += splitType[i];
    }
    return output.join(delimiter);
};