<template>
  <div>
    <div v-for="(item, index) in items" :id="index">
      <span
        class="extensible-span"
        draggable="true"
        v-on:dragstart="dragStart($event, index)"
        v-on:dragover="dragOver"
        v-on:drop="drop($event, index)"
        v-on:click="extend">
        {{ item.item }}
      </span>
      <div class="extensible-content">测试内容 {{item.item }}</div>
    </div>

    <el-collapse v-model="activeName" accordion>
      <el-collapse-item v-for="(item, index) in items" :key="index" :title="item.item" :name="index">
        <div>测试内容 {{item.item }}</div>
      </el-collapse-item>
    </el-collapse>
    <el-collapse v-model="activeName" accordion>
      <el-collapse-item title="一致性 Consistency" name="1">
        <div>与现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；</div>
        <div>在界面中一致：所有的元素和结构需保持一致，比如：设计样式、图标和文本、元素的位置等。</div>
      </el-collapse-item>
      <el-collapse-item title="反馈 Feedback" name="2">
        <div>控制反馈：通过界面样式和交互动效让用户可以清晰的感知自己的操作；</div>
        <div>页面反馈：操作后，通过页面元素的变化清晰地展现当前状态。</div>
      </el-collapse-item>
      <el-collapse-item title="效率 Efficiency" name="3">
        <div>简化流程：设计简洁直观的操作流程；</div>
        <div>清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策；</div>
        <div>帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担。</div>
      </el-collapse-item>
      <el-collapse-item title="可控 Controllability" name="4">
        <div>用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；</div>
        <div>结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。</div>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>

  import ElCollapse from "element-ui/packages/collapse/src/collapse";
  import ElCollapseItem from "element-ui/packages/collapse/src/collapse-item";
  import CollapseTransition from 'element-ui/lib/transitions/collapse-transition';
  import Vue from 'vue'

  Vue.component(CollapseTransition.name, CollapseTransition)

  export default {
    components: {
      ElCollapseItem,
      ElCollapse,},
    name: "extensible-item",
    data() {
      return {
        items: [{
          item: "测试项0"
        },{
          item: "测试项1"
        },{
          item: "测试项2"
        }],
        dropItemId: 0,
        activeName: 1
      }
    },
    methods: {
      extend(event) {
        // $(event.target).parent().children(".extensible-content").toggle(500);
      },
      dragStart(event, index) {
        this.dropItemId = index;
      },
      dragOver(event) {
        event.preventDefault();
      },
      drop(event, index) {
        event.preventDefault();
        let itemData = this.items.splice(this.dropItemId, 1);
        this.items.splice(index, 0, itemData[0]);
      }
    }


  }
</script>

<style>
  /*div .extensible-content {*/
    /*border-style: none solid solid solid;*/
  /*}*/

  .el-collapse {
    z-index: 3;
  }
</style>
