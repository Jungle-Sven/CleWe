import classNames from "classnames";
import layout from "../../../layout.module.css";
import ToolBox from "./ToolBox";

type Params = {
  id: string;
  slug: string;
};

const quests = [
  {
    title: "Blockchain Quiz",
    id: "640f4bd645c1c80018e9e8aa",
  },
  {
    title: "DEX quiz",
    id: "64146c6ed6a2be0018c1a6c8",
  },
  {
    title: "Wallets quiz",
    id: "64146f1fd6a2be0018c1ad73",
  },
];

function resolveQuestBySlug(slug: string) {
  const decodedSlug = decodeURIComponent(slug);
  const quizNumber = decodedSlug.split(":")[1].trim();
  return quests[Number(quizNumber)];
}

export default function Page({ params }: { params: Params }) {
  const quest = resolveQuestBySlug(params.slug);
  return (
    <>
      <div className={classNames(layout.fullWidth)}>
        <iframe
          width="100%"
          height={650}
          title={quest.title}
          src={`https://view.genial.ly/${quest.id}`}
          itemType="text/html"
          scrolling="yes"
        ></iframe>
      </div>
      <ToolBox slug={params.slug} userId={params.id} />
    </>
  );
}
